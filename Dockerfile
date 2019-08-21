FROM python:3
ADD python_assignment.py /
ADD quiz.json /
CMD [ "python", "./python_assignment.py" ]