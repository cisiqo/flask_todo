#!/usr/bin/env python
# coding: utf-8

from todo import app
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from datetime import datetime    
import todo.db

def get_by_id(id):
    db = todo.db.get_db()
    cur = db.execute('select * from todo where id=?',[id])
    s = cur.fetchone()
    if not s:
        return False
    return s

@app.route('/')
def show_todos():
    db = todo.db.get_db()
    cur = db.execute('select * from todo order by finished asc, id asc')
    todos = cur.fetchall()
    return render_template('index.html', todos=todos, app=app)


@app.route('/todo/new', methods=['POST'])
def add_todo():
    title = request.form['title']
    if not title:
        return render_template('error.html', content="标题是必须的",url=None)
    db = todo.db.get_db()
    db.execute('insert into todo (title, post_date) values (?, ?)',
                   [title, datetime.now()])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_todos'))
    
    
@app.route('/todo/<int:id>/delete', methods=['GET'])
def delete(id):
    if not todo:
        return render_template('error.html', content="没找到这条记录",url=None)
    db = todo.db.get_db()
    db.execute('delete from todo where id=?',[id])
    return render_template('error.html', content="删除成功！",url='/')


@app.route('/todo/<int:id>/finish', methods=['GET'])
def finish(id):
    if not todo:
        return render_template('error.html', content="没找到这条记录",url=None)
    status = request.args.get('status')
    if status == 'yes':
        finished = 1
    elif status == 'no':
        finished = 0
    else:
        return render_template('error.html', content="您发起了一个不允许的请求",url='/')
    db = todo.db.get_db()
    db.execute('update todo set finished=? where id=?',
                   [finished, id])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_todos'))


@app.route('/todo/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    onetodo = get_by_id(id)
    if not onetodo:
        return render_template('error.html', content="没找到这条记录",url=None)
    if request.method == 'GET':
        return render_template('todo/edit.html', todo=onetodo, app=app)
    else:
        title = request.form['title']
        if not title:
            return render_template('error.html', content="标题是必须的",url=None)
        db = todo.db.get_db()
        db.execute('update todo set title=? where id=?',
                       [title, id])
        db.commit()
        flash('Edit todo was successfully posted')
        return redirect(url_for('show_todos'))
     
        
        
