
from basic import db, Course

db.create_all()

rust = Course('Learn Rust from Scratch', 8,
              'This is some text explaninig course about Rust programming language')
pythy = Course('Learn Python 3 from Scratch', 1,
               'This is some new paragraph explaninig what is new in Python 3')

db.session.add_all([rust, pythy])

db.session.commit()
