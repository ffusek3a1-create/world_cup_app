from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Definiujemy adres bazy (plik powstanie w folderze backend)
DATABASE_URL = "sqlite:///./world_cup.db"

# 2. Tworzymy silnik bazy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Tworzymy fabrykę sesji (do rozmowy z bazą)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Tworzymy obiekt Base - to jest fundament, którego brakowało!
Base = declarative_base()

# 5. Definicja tabeli drużyn
class Team(Base):
    __tablename__ = "teams"
    id           = Column(Integer, primary_key=True, index=True)
    name         = Column(String, unique=True)
    group        = Column(String)
    fifa_ranking = Column(Integer)
    manager      = Column(String)
    nickname     = Column(String)

# 6. Polecenie faktycznego stworzenia pliku na dysku
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Baza danych została utworzona!")