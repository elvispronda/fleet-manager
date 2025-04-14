from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .api import auth, vehicle, fuel_log, maintenance, budget, trip, fuel
from .models import user, vehicle as vmodel, fuel_log as flog, maintenance as maint, budget as budg, trip as tmodel, fuel as fmodel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fleet Management System API")

# Optional: CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(vehicle.router, prefix="/api/vehicles", tags=["Vehicles"])
app.include_router(fuel_log.router, prefix="/api/fuel-log", tags=["Fuel Log"])
app.include_router(maintenance.router, prefix="/api/maintenance", tags=["Maintenance"])
app.include_router(budget.router, prefix="/api/budget", tags=["Budget & Cost"])
app.include_router(trip.router, prefix="/api/trips", tags=["Trips"])
app.include_router(fuel.router, prefix="/api/fuels", tags=["Fuels"])
