from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from wtforms import  fields, validators 
from wtforms.validators import Length, Email
from sqlalchemy.orm import relationship
from datetime import datetime
import bcrypt

import re 
db = SQLAlchemy()