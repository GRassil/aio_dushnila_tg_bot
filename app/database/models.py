from sqlalchemy import DateTime, ForeignKey, String, Text, BigInteger, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class Role(Base):
    __tablename__ = "role"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __init__(self, name):

        self.name = name


class Profession(Base):
    __tablename__ = "profession"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __init__(self, name):

        self.name = name


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    fullname: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    role_id: Mapped[int] = mapped_column(
        ForeignKey("role.id", ondelete="CASCADE"), nullable=False, default=1
    )
    profession_id: Mapped[int] = mapped_column(
        ForeignKey("profession.id", ondelete="CASCADE"), nullable=False
    )
    subject_ids: Mapped[str] = mapped_column(nullable=False)

    role: Mapped["Role"] = relationship(backref="user")
    profession: Mapped["Profession"] = relationship(backref="user")

    def __init__(self, user_id, username, fullname, role_id, profession_id, subjects):
        self.user_id = user_id
        self.fullname = fullname
        self.username = username
        self.role_id = role_id
        self.profession_id = profession_id
        self.subject_ids = subjects


class Subject(Base):
    __tablename__ = "subject"

    name: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    num_of_questions: Mapped[int]

    def __init__(self, name, num_of_questions):
        self.name = name
        self.num_of_questions = num_of_questions


class Course(Base):
    __tablename__ = "course"

    name: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False, default=0)


class Theory(Base):
    __tablename__ = "theory"

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE"), nullable=False
    )
    file_id: Mapped[str] = mapped_column(Text, nullable=False)

    subject: Mapped["Subject"] = relationship(backref="theory")


class Exercise(Base):
    __tablename__ = "exercise"

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE"), nullable=False
    )
    description: Mapped[str] = mapped_column(Text)
    photo_id: Mapped[str] = mapped_column(Text)
    num_of_ex_in_test: Mapped[int] = mapped_column(nullable=False)
    right_answer: Mapped[str] = mapped_column(String(50), nullable=False)
    total_attempts: Mapped[int] = mapped_column(default=0)
    right_attempts: Mapped[int] = mapped_column(default=0)

    subject: Mapped["Subject"] = relationship(backref="exercise")


class Homework1part(Base):
    __tablename__ = "homework1"

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE"), nullable=False
    )
    file_id: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    right_answer: Mapped[str] = mapped_column(String(50), nullable=False)
    total_attempts: Mapped[int] = mapped_column(default=0)
    right_attempts: Mapped[int] = mapped_column(default=0)

    subject: Mapped["Subject"] = relationship(backref="homework1")


class UserHomework1part(Base):
    __tablename__ = "user_hw_res1"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    homework_id: Mapped[int] = mapped_column(
        ForeignKey("homework1.id", ondelete="CASCADE")
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE")
    )
    answers_1part: Mapped[str] = mapped_column(String(150), nullable=False)
    result_1part: Mapped[str] = mapped_column(String(150), nullable=False)
    student_file_id: Mapped[str] = mapped_column(Text)
    teacher_file_id: Mapped[str] = mapped_column(Text)
    points: Mapped[int] = mapped_column(default=0)

    user: Mapped["User"] = relationship(backref="user_hw_res1")
    subject: Mapped["Subject"] = relationship(backref="user_hw_res1")
    homework: Mapped["Homework1part"] = relationship(backref="user_hw_res1")


class Homework2part(Base):
    __tablename__ = "homework2"

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE"), nullable=False
    )
    file_id: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    total_attempts: Mapped[int] = mapped_column(default=0)
    right_attempts: Mapped[int] = mapped_column(default=0)

    subject: Mapped["Subject"] = relationship(backref="homework2")


class UserHomework2part(Base):
    __tablename__ = "user_hw_res2"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    homework_id: Mapped[int] = mapped_column(
        ForeignKey("homework2.id", ondelete="CASCADE")
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE")
    )
    student_file_id: Mapped[str] = mapped_column(Text)
    teacher_file_id: Mapped[str] = mapped_column(Text)
    points: Mapped[int] = mapped_column(default=0)

    user: Mapped["User"] = relationship(backref="user_hw_res2")
    homework: Mapped["Homework2part"] = relationship(backref="user_hw_res2")
    subject: Mapped["Subject"] = relationship(backref="user_hw_res2")


class Test(Base):
    __tablename__ = "test"

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE"), nullable=False
    )
    file_id: Mapped[str] = mapped_column(Text)

    subject: Mapped["Subject"] = relationship(backref="Test")


class UserTestResult(Base):
    __tablename__ = "user_test_res"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    test_id: Mapped[int] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE")
    )
    answers_1part: Mapped[str] = mapped_column(String(150), nullable=False)
    result_1part: Mapped[str] = mapped_column(String(150), nullable=False)
    student_file_id: Mapped[str] = mapped_column(Text)
    teacher_file_id: Mapped[str] = mapped_column(Text)
    points_of_1part: Mapped[int] = mapped_column(default=0)
    points_of_2part: Mapped[int] = mapped_column(default=0)

    user: Mapped["User"] = relationship(backref="user_test_res")
    test: Mapped["Test"] = relationship(backref="user_test_res")
    subject: Mapped["Subject"] = relationship(backref="user_test_res")
