from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from models.machine import MachineModel
from serializers.machine import machineSchema
from services.digital_twin import DigitalTwin
from typing import List
from database import get_db

router = APIRouter()


@router.get("/machines", response_model=List[machineSchema])
def get_machines(db: Session = Depends(get_db)):
    machines = db.query(MachineModel).all()
    return machines



@router.get("/machines/{machien_id}", response_model=machineSchema)
def get_single_machine(machine_id: int, db: Session = Depends(get_db)):
    machine = db.query(MachineModel).filter(MachineModel.machine_id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine



@router.post("/machines/{machine_id}/start")
def start_machine_stream(machine_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    machine = db.query(MachineModel).filter(MachineModel.machine_id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    digital_twin = DigitalTwin(machine_id=machine_id, db=db)

    background_tasks.add_task(digital_twin.start_stream)


    return {"message": f"Digital twin stream started for machine {machine_id}"}





