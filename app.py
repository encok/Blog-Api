from flask import Flask, request, jsonify

app = Flask(__name__)

blogs_list = [
    {
      "id": 0,
      "author": "enock kipronoh",
      "language": "English",
      "title": "Gender Equality",
      "description": "Gender equality, also known as sexual equality or equality of the sexes, is the state of equal ease of access to resources and opportunities regardless of gender, including economic participation and decision-making; and the state of valuing different behaviors, aspirations and needs equally, regardless of gender."
    }
    

]