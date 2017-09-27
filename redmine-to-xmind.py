#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from redmine import Redmine
import xmind
from xmind.core import workbook,saver
from xmind.core.topic import TopicElement
import time
rmUrl = 'http://rm.site.ru'
rmKey = 'herebethekey'
rmProjectName = 'trade'

redmine = Redmine(rmUrl, key=rmKey)
project = redmine.project.get(rmProjectName)
issues = redmine.issue.filter(project_id = project.id, status_id = 'open')

workbook = xmind.load('redmine.xmind')

sheet = workbook.getPrimarySheet()
sheet.setTitle('Задачи')
root = sheet.getRootTopic()
root.setTitle('Задачи')

issuesByAuthors = defaultdict(list)
for issue in issues:
    if not issuesByAuthors[issue.author.name]:
        issuesByAuthors[issue.author.name] = TopicElement()
        issuesByAuthors[issue.author.name].setTitle(
            issue.author.name.encode('utf-8')
            )
        issuesByAuthors[issue.author.name].setFolded()
    issueTopic = TopicElement()
    title = '%d: %s' % (issue.id, issue.subject.encode('utf-8'))
    issueTopic.setTitle(title)
    try:
        assigned_to = issue.assigned_to
    except:
        assigned_to = ""
    note = ('Ответственный: %s\nДата создания: %s\nОписание: %s'
        % (assigned_to, issue.created_on, 
        issue.description.encode('utf-8'))
        )
    for attachment in issue.attachments:
        attachmentTopic = TopicElement()
        attachmentTopic.setTitle(
            "Вложение: " + attachment.filename.encode('utf-8')
            )
        attachmentTopic.setFileHyperlink(attachment.content_url)
        issueTopic.addSubTopic(attachmentTopic)
    issueTopic.setPlainNotes(note)
    issuesByAuthors[issue.author.name].addSubTopic(issueTopic)

[root.addSubTopic(topic) for topic in issuesByAuthors.values()]

xmind.save(workbook, 'redmine.xmind')
