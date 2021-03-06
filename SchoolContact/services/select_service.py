# coding: UTF-8

from SchoolContact.models.students import StudentsClass as Student
from SchoolContact.models.industry import Industry
from SchoolContact import db
from sqlalchemy import or_,and_,LargeBinary


def get_student_all():
    '''获取所有学生'''
    student_all = Student.query.filter().all()
    return student_all


def get_student_by_industry(industry):
    '''根据行业获取'''
    result_count = db.query(Student)\
        .join(Industry)\
    .filter(Industry.id == industry).count()


#def select_student_count(enter_time,industry_id):
#     '''根据查询条件获取学生数'''
#     student_selected_count = Student.query.filter(Student.stu_enter_time == enter_time,Student.industry_id==industry_id).count()
#     return student_selected_count
#def select_student_all(enter_time,industry_id):
#    '''查询到多个学生'''
#    student_selected = Student.query.filter(Student.stu_enter_time == enter_time,Student.industry_id==industry_id).all()
#    return student_selected
#
#def select_student_first(enter_time,industry_id):
#    '''查询到一个学生 '''
#    student_selected = Student.query.filter(Student.stu_enter_time == enter_time,Student.industry_id==industry_id).first()
#    return student_selected

def vague_count(trade,para):
    #模糊查询
    student_count = get_student_count(trade,para)
    return student_count

def get_student_count(trade,para):
    #其他条件查询
     student_count = Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like(LargeBinary('%'+para+'%')),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%')),and_(Student.industry_id==trade)).count()
     return  student_count


#全部行业查询到的数量

def vague_with_no_trade_count(para):
    #模糊查询
    student_count = get_student_with_no_trade_count(para)
    return student_count

def get_student_with_no_trade_count(para):
    #其他条件查询
     student_count = Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like(LargeBinary('%'+para+'%')),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%'))).count()
     return  student_count




#def get_industry_count(para):
#    #根据行业查询
#       industry = Industry.query.filter(Industry.industry_name.like('%'+para+'%')).first()
#       id = industry.id
#       student_count = Student.query.filter(Student.industry_id == id).count()
#       return student_count

#def get_by_industry(para):
#
#     industry = Industry.query.filter(Industry.industry_name.like('%'+para+'%')).first()
#     id = industry.id
#     student_count = Student.query.filter(Student.industry_id == id).count()
#     if student_count > 1:
#         student = Student.query.filter(Student.industry_id == id).all()
#     else:
#         student = Student.query.filter(Student.industry_id == id).first()
#
#     return student

def vague_first(trade,para):
    #查询到一个
    # student_count = get_student_count(trade,para)
    # if student_count < 1:
    #   student_first = get_by_industry(trade,para)
    #    if student_first <1:
    #         student_first = None
    #     else:
    #         pass
    # else:
     student_first =Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like (LargeBinary('%'+para+'%')),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%')),and_(Student.industry_id==trade)).first()
     return student_first
def vague_all(trade,para,current_page,per_page):
     #查询到多条
     #student_count = get_student_count(trade,para)
     student_all =Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like (LargeBinary('%'+para+'%')),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%')),and_(Student.industry_id == trade))[per_page*(current_page-1):per_page*current_page]

     return student_all


#全部行业查询
def vague_with_no_trade_first(para):
    #查询到一个
    # student_count = get_student_count(trade,para)
    # if student_count < 1:
    #   student_first = get_by_industry(trade,para)
    #    if student_first <1:
    #         student_first = None
    #     else:
    #         pass
    # else:
     student_first =Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like (LargeBinary('%'+para+'%')),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%'))).first()
     return student_first
def vague_with_no_trade_all(para,current_page,per_page):
     #查询到多条
     #student_count = get_student_count(trade,para)
     student_all =Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like (LargeBinary('%'+para+'%')),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%')))[per_page*(current_page-1):per_page*current_page]

     return student_all

