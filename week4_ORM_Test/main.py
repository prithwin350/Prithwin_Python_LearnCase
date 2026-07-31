import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,sessionmaker

engine = db.create_engine("sqlite:///students.db")
Session = sessionmaker(bind=engine)



class Base(DeclarativeBase):
    pass

class Students(Base):
    __tablename__="students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[int]

def add_student(name,value):
    print("adding students")
    session=Session()
    try:
        student=Students(name=name,value=value)
        session.add(student)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def view_students():
    session=Session()
    try:
        students=session.query(Students).all()
        return students
    finally:
        session.close()


def update_students(student_id,name,value):
    session=Session()
    try:
        student=session.get(Students,student_id)
        if student is None:
            return False
        student.name=name
        student.value=value
        session.commit()
    except Exception as e: 
        print(e)
        session.rollback()
    finally:
        session.close()

def delete_students(student_id):
    session=Session()
    try:
        student=session.get(Students,student_id)
        session.delete(student)
        session.commit()
        return True
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def create_db():
    Base.metadata.create_all(engine)
    

def main():
    print("This is a main function")
    print(db.__version__)
    create_db()

if __name__=="__main__":
    main()