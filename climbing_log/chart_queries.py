from climbing_log import db
from climbing_log.models import Sessions, Climb
from sqlalchemy import func
import pandas as pd
from collections import Counter
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px

# list of grades in difficulty order for axis of plots
grades_correct_order = [
    "4",
    "5",
    "5+",
    "6A",
    "6A+",
    "6B",
    "6B+",
    "6C",
    "6C+",
    "7A",
    "7A+",
    "7B",
    "7B+",
    "7C",
    "7C+",
    "8A",
    "8A+",
    "8B",
    "8B+",
    "8C",
    "8C+",
    "9A"
]


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
        'Status': ['Climbs Completed', 'Climbs NOT Completed'],
        'Amount': [completed_count, not_completed_count]
    })
    # use plotly to create the pie chart using the dataframe
    fig = px.pie(df, names='Status', values='Amount')
    fig.update_layout(
        # change text/graph line colors and font
        font_color='rgb(255, 255, 255)',
        font_family="Kanit",
        # change background colors
        paper_bgcolor='rgb(68, 68, 68, 0.7)',
        plot_bgcolor='rgb(68, 68, 68, 0.7)',
        # set white space around plot
        margin_l=10,
        margin_r=20,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="right",
            x=0.95,
            bgcolor = 'rgba(68, 68, 68, 0.0)'))
    # remove text from pie
    fig.update_traces(textinfo='none')
    # convert the plotly figure to JSON
    pie_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    return pie_json


def get_range_of_difficulty_climbed(session_id):
    # get data of all completed climbs from the session
    climbs = Climb.query.filter_by(
        session_id=session_id).filter_by(completed=True).all()
    # empty list to hold grades
    grades = []
    # loop through climbs completed appending grade to list
    for climb in climbs:
        grades.append(climb.difficulty)
    count_grades = Counter(grades)
    grades = list(count_grades.keys())
    number_of_each_grade = list(count_grades.values())

    bar_labels = {'x': 'Grade', 'y': 'Number Climbed'}
    # create bar chart using data
    if grades:
        fig = px.bar(x=grades, y=number_of_each_grade, labels=bar_labels)
        fig.update_layout(
            # change text/graph line colors and font
            font_color='rgb(255, 255, 255)',
            font_family="Kanit",
            # change background colors
            paper_bgcolor='rgb(68, 68, 68, 0.7)',
            plot_bgcolor='rgb(68, 68, 68, 0.7)',
            # set white space around plot
            margin_l=10,
            margin_r=20,
            # set legend background color
            legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="right",
            x=0.95,
            bgcolor = 'rgba(68, 68, 68, 0.0)'))
        
        fig.update_yaxes(showgrid=False)

        # this code filters the grade list for ones which have a value
        # to remove empty grades from x axis but ensure correct order of grades

        grades_present_in_chart = []

        for grade in grades_correct_order:
            if grade in grades:
                grades_present_in_chart.append(grade)

        fig.update_xaxes(categoryorder='array',
                         categoryarray=grades_present_in_chart)
        bar_grades = json.dumps(fig, cls=PlotlyJSONEncoder)

        return bar_grades
    else:
        return None


def get_range_of_difficulty_not_climbed(session_id):
    # get data of all completed climbs from the session
    climbs = Climb.query.filter_by(
        session_id=session_id).filter_by(completed=False).all()
    # empty list to hold grades
    grades = []
    # loop through climbs completed appending grade to list
    for climb in climbs:
        grades.append(climb.difficulty)
    count_grades = Counter(grades)
    grades = list(count_grades.keys())
    number_of_each_grade = list(count_grades.values())

    bar_labels = {'x': 'Grade', 'y': 'Failed Attempts'}
    # create bar chart using data
    if grades:
        fig = px.bar(x=grades, y=number_of_each_grade, labels=bar_labels)
        fig.update_layout(
            # change text/graph line colors and font
            font_color='rgb(255, 255, 255)',
            font_family="Kanit",
            # change background colors
            paper_bgcolor='rgb(68, 68, 68, 0.7)',
            plot_bgcolor='rgb(68, 68, 68, 0.7)',
            # set white space around plot
            margin_l=10,
            margin_r=20
        )

        fig.update_yaxes(showgrid=False)
        # this code filters the grade list for ones which have a value
        # to remove empty grades from x axis but ensure correct order of grades

        grades_present_in_chart = []

        for grade in grades_correct_order:
            if grade in grades:
                grades_present_in_chart.append(grade)
        fig.update_xaxes(categoryorder='array',
                         categoryarray=grades_correct_order)
        bar_grades = json.dumps(fig, cls=PlotlyJSONEncoder)

        return bar_grades
    else:
        return None


def get_range_of_length_climbs(session_id):

    # query database for climb details from the relevant session
    climbs = Climb.query.filter_by(session_id=session_id).all()

    grade = []
    length = []
    completed = []

    for climb in climbs:
        grade.append(climb.difficulty)
        length.append(climb.length)
        completed.append(climb.completed)
    # labels for axis
    scatter_labels = {'x': 'Grade', 'y': 'Number of Moves'}

    # change values of completed climb from true/false to yes/no for fig legend
    figure_labels = []
    for climb in completed:
        if climb:
            figure_labels.append('Yes')
        else:
            figure_labels.append('No')
    # create figure
    fig = px.scatter(x=grade, y=length, color=figure_labels,
                     labels=scatter_labels)
    # pass the grades as an array to ensure they are displayed in correct order
    fig.update_xaxes(categoryorder='array',
                     categoryarray=grades_correct_order)

    fig.update_layout(
        # change text/graph line colors and font
        font_color='rgb(255, 255, 255)',
        font_family="Kanit",
        # change background colors
        paper_bgcolor='rgb(68, 68, 68, 0.7)',
        plot_bgcolor='rgb(68, 68, 68, 0.7)',
        # set white space around plot
        margin_l=10,
        margin_r=20,
        # customise legend text/position
        legend=dict(
            title='Climbed succesfully?',
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="center",
            x=0.5,
        )
    )
    # change style of markers
    fig.update_traces(marker=dict(size=12,
                                  line=dict(width=2,
                                            color='rgb(255, 255, 255)')))

    # create json of figure
    scatter = json.dumps(fig, cls=PlotlyJSONEncoder)
    return scatter
