from climbing_log import db
from climbing_log.models import Users, Sessions, Climb
from sqlalchemy import func
from sqlalchemy.orm import joinedload
import pandas as pd
from collections import Counter
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px

def get_completed_uncompleted_climbs(session_id):
        # get data from database for chart
        last_session = Sessions.query.filter_by(session_id=session_id).first()
        # get number of climbs completed from most recent session
        completed_count = db.session.query(func.count(Climb.climb_id)).filter_by(
            session_id=last_session.session_id, completed=True).scalar()
        # get number of climbs not completed from most recent session
        not_completed_count = db.session.query(func.count(Climb.climb_id)).filter_by(
            session_id=last_session.session_id, completed=False).scalar()
        # use pandas to create the dataframe
        df = pd.DataFrame({
            'Status': ['Climbs completed', 'Climbs NOT completed'],
            'Amount': [completed_count, not_completed_count]
        })
        # use plotly to create the pie chart using the dataframe
        fig = px.pie(df, names='Status', values='Amount')
        fig.update_layout(
            margin=dict(t=0, b=0, l=0, r=0),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=0.01,
                xanchor="right",
                x=0.95))
        # convert the plotly figure to JSON
        pie_json = json.dumps(fig, cls=PlotlyJSONEncoder)
        return pie_json 

def get_range_of_difficulty_climbed(session_id):
        # get data of all completed climbs from the session
        climbs = Climb.query.filter_by(session_id=session_id).filter_by(completed=True).all()
        # empty list to hold grades
        grades = []
        # loop through climbs completed appending grade to list
        for climb in climbs:
                grades.append(climb.difficulty)
        count_grades = Counter(grades)
        grades = list(count_grades.keys())
        number_of_each_grade = list(count_grades.values())
        # to check grades/count match correctly !!!!! remember to remove
        # zipped_list = list(zip(grades, number_of_each_grade))
        bar_labels = {'x':'Grade', 'y':'Number climbed'}
        #create bar chart using data
        fig = px.bar(x=grades,y=number_of_each_grade,labels=bar_labels)
        bar_grades = json.dumps(fig, cls=PlotlyJSONEncoder)
        
        return bar_grades


def get_range_of_length_climbs(session_id):
        climbs = Climb.query.filter_by(session_id=session_id).all()
        climb_lengths = []
        for climb in climbs:
                climb_lengths.append(climb.length)
        return climb_lengths
        
     



        
                