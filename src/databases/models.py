from sqlalchemy import Column, DateTime, func


class CommonMixin:
    def save(self, db):
        if self.id:  # update
            db.commit()
            return self
        else:  # create
            db.add(self)
            db.commit()
            db.refresh(self)
            return self


class CreatedAtMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class DatetimeMixin(CreatedAtMixin):
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
