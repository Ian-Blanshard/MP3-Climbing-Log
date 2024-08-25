from climbing_log import db
from climbing_log.models import Users, Sessions, Climb
from sqlalchemy import func
from sqlalchemy.orm import joinedload
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px

def get_completed_uncompleted_climbs(session_id):
        # get data from database for chart
        # get the most recent session
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