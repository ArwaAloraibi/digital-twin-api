from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.machine import MachineModel
from serializers.machine import machineSchema
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



# @router.post("/teas", response_model=TeaSchema)
# def create_tea(tea: TeaSchema, db: Session = Depends(get_db)):
#     new_tea = TeaModel(**tea.dict()) # Convert Pydantic model to SQLAlchemy model
#     db.add(new_tea)
#     db.commit() # Save to database
#     db.refresh(new_tea) # Refresh to get the updated data (including auto-generated fields)
#     return new_tea





