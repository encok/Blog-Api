from flask import Flask, request, jsonify

app = Flask(__name__)

blogs_list = [
    {
      "id": 0,
      "author": "enock kipronoh",
      "language": "English",
      "title": "Gender Equality",
      "description": "Gender equality, also known as sexual equality or equality of the sexes, is the state of equal ease of access to resources and opportunities regardless of gender, including economic participation and decision-making; and the state of valuing different behaviors, aspirations and needs equally, regardless of gender."
    },
      {
      "id": 2,
      "author": "Jonson Nyang'au",
      "language": "English",
      "title": "The future of Python-Flask",
      "description": "Python will be the language of the future. Testers will have to upgrade their skills and learn these languages to tame the AI and ML tools. Python might not have bright years in the past years (which is mainly launch in the year 1991) but it has seen a continuous and amazing trend of growth in the 21st century."
    },
      {
      "id": 3,
      "author": "Hellen Mutisya",
      "language": "English",
      "title": "The Current Economy",
      "description": "The Economy of Kenya is a market-based economy with a few state enterprises. Major industries include agriculture, forestry, fishing, mining, manufacturing, energy, tourism and financial services."
    },
    

]