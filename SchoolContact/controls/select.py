# coding: UTf-8
from flask import request, render_template
from SchoolContact.services.select_service import *
from SchoolContact.services.student_service import *
from SchoolContact.models.industry import *

def to_select_page():
    '''到结识校友'''
    student_all = get_student_all() #得到所有学生信息
    if student_all:
        return render_template('all_student.html',
                               student_all=student_all)
    return render_template('all_student.html',
                           marked='yes')


#def select_student():
    #'''根据行业查找'''
    #industry = request.args.get('industry') # 获取web端传如参数
    #student_all = get_student_by_industry(industry)
    #return render_template('all_student.html',
     #                      student_all=student_all)

   # trade =int(request.form.get('trade'))
    #enter_time =request.form.get('e_time')
    #student_selected_count = select_student_count(enter_time,trade)
    #if student_selected_count > 1:
     #   student_selected = select_student_all(enter_time,trade)
    #else:
     #    student_selected = select_student_first(enter_time,trade)
    #return render_template('search.html',student_selected = student_selected,student_count = student_selected_count)


#关键字查询 ，模糊查询
def vague_select():
    trade = request.form.get('trade')
    para = request.form.get('para')
    student_count = vague_count(trade,para)
    if student_count > 1:
        student_selected = vague_all(trade,para)
    else:
        student_selected = vague_first(trade,para)


    industry_count = Industry.query.filter().count()
    if industry_count >1:
        industry = Industry.query.filter().all()
    else:
        industry = Industry.query.filter().first()
    return render_template('search.html',student_selected = student_selected,student_count = student_count,industry=industry,industry_count=industry_count)

