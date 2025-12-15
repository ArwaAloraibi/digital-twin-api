from sqlalchemy.orm import Session
from database import get_db
from services.digital_twin import DigitalTwin

# Get a database session
db: Session = next(get_db())

# Create DigitalTwin for machine 15
digital_twin = DigitalTwin(machine_id=15, db=db)

# Start streaming (it will print risk and efficiency every 2 seconds)
digital_twin.start_stream(interval_sec=2)
