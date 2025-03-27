from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, sandwich):

    db_sandwiches = models.Sandwich(
        sandwich_name=sandwich.name,
        price=sandwich.price,
    )

    db.add(db_sandwiches)

    db.commit()

    db.refresh(db_sandwiches)

    return db_sandwiches


def read_all(db: Session):
    return db.query(models.Sandwich).all()


def read_one(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()


def update(db: Session, sandwich_id, sandwich):

    db_sandwiches = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

    update_data = sandwich.dict(exclude_unset=True)

    db_sandwiches.update(update_data, synchronize_session=False)

    db.commit()

    return db_sandwiches.first()


def delete(db: Session, sandwich_id):

    db_order = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

    db_order.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)