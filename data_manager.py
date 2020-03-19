import connection
import util
from operator import itemgetter


@connection.connection_handler
def get_answers(cursor, question_id=None):
    if question_id:
        cursor.execute("""SELECT * FROM answer WHERE question_id = (%s)""", (question_id,))
        answers = [dict(row) for row in cursor.fetchall()]
    else:
        cursor.execute("""SELECT * FROM answer""")
        answers = [dict(row) for row in cursor.fetchall()]
    return answers


@connection.connection_handler
def get_questions(cursor, question_id=None):
    if not question_id:
        cursor.execute("""SELECT * FROM question """)
        questions = [dict(row) for row in cursor.fetchall()]
    else:
        cursor.execute("""SELECT * FROM question WHERE id = (%s)""", (question_id,))
        questions = [dict(row) for row in cursor.fetchall()]
    return questions


@connection.connection_handler
def search_by_title_or_message(cursor, text):
    text = '%' + text + '%'
    cursor.execute("""SELECT * FROM question WHERE (message LIKE (%s)) OR (title LIKE (%s))""", (text, text,))
    searched_list = [dict(row) for row in cursor.fetchall()]
    if len(searched_list) == 0:
        cursor.execute("""SELECT * FROM question """, )
        searched_list = [dict(row) for row in cursor.fetchall()]
    return searched_list


@connection.connection_handler
def get_comments(cursor, question_id):
    cursor.execute("""SELECT * FROM comment WHERE question_id = (%s)""", (question_id,))
    comments = [dict(row) for row in cursor.fetchall()]
    return comments


@connection.connection_handler
def new_question_manager(cursor, new_question, user_email):
    cursor.execute("""INSERT INTO question (title,submission_time, message, user_email) VALUES (%s,%s,%s,%s);""",
                   (new_question['title'], util.submission_time(), new_question['message'], user_email))
    cursor.execute("""SELECT id FROM question WHERE title= %(title)s;""",
                   {'title': new_question['title'], 'message': new_question['message']})
    question_id = dict(cursor.fetchone())['id']
    return question_id


@connection.connection_handler
def new_answer_manager(cursor, new_answer):
    cursor.execute(
        """INSERT INTO answer (submission_time, question_id, message, user_email)  VALUES ( %s, %s, %s, %s);"""
        , (util.submission_time(), new_answer['question_id'], new_answer['message'], new_answer['user_email']))
    return new_answer['question_id']


@connection.connection_handler
def new_comment_manager(cursor, new_comment):
    if new_comment['question_id'] or new_comment['question_id'] == 0:
        new_message_value = new_comment['question_id']
        new_message = 'question_id'
    else:
        new_message_value = new_comment['answer_id']
        new_message = 'answer_id'

    cursor.execute("""INSERT INTO comment (submission_time, question_id, message)  VALUES ( %s, %s, %s);""",
                   (util.submission_time(), new_message_value, new_comment['message'],))


@connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("""DELETE FROM question WHERE id = (%s)""", (question_id,))


@connection.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute("""DELETE FROM answer WHERE id = (%s)""", (answer_id,))


@connection.connection_handler
def update_question(cursor, question_id, new_question):
    cursor.execute("""UPDATE question SET message=(%s), title=(%s) WHERE id=(%s);""",
                   (new_question['message'], new_question['title'], question_id,))
    return question_id


@connection.connection_handler
def update_answer(cursor, answer_id, new_answer):
    cursor.execute("""UPDATE answer SET message=(%s) WHERE id = (%s);""", (new_answer['message'], answer_id,))
    cursor.execute(""" SELECT question_id FROM answer WHERE id=(%s);""", (answer_id,))
    question_id = cursor.fetchone()
    return question_id


@connection.connection_handler
def add_user(cursor, new_user):
    hashed_password = util.hash_password(new_user['password'])

    cursor.execute("""INSERT INTO users (email, hash, registration_time) VALUES (%s, %s, %s);""",
                   (new_user['email'], hashed_password, util.submission_time()))


@connection.connection_handler
def get_user_email(cursor, data_id, table):
    sql = """SELECT user_email FROM """ + table + """ WHERE id = """ + str(data_id)
    cursor.execute(sql)
    user_email = cursor.fetchall()
    return user_email[0]['user_email']


@connection.connection_handler
def get_user_password_by_email(cursor, email):
    cursor.execute("""SELECT hash FROM users WHERE email = (%s);""", (email,))
    user_hash = cursor.fetchall()
    if user_hash:
        user_hash = user_hash[0]['hash']
    else:
        user_hash = util.hash_password('wrong password')

    return user_hash


@connection.connection_handler
def get_session_user(cursor, user_email):
    query = f"""
    SELECT users.id , users.email, users.registration_time, 
    COUNT(question.user_email) as questions_counter, COUNT(answer.user_email) as answers_counter FROM users
    LEFT JOIN question ON users.email = question.user_email LEFT JOIN answer ON users.email = answer.user_email
    WHERE users.email = '{user_email}'
    GROUP BY users.id ;"""

    cursor.execute(query)
    users = cursor.fetchall()
    users_data = [dict(user) for user in users]

    return users_data
