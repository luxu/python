from scrapinghub import ScrapinghubClient
import scrapinghub as sh
import configparser

'''
Programa que serve para gerenciamento do site SCRAPINGHUB.COM
'''

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')

apikey = u'a103bede59104d20a3fcdd4573996355'
spider_ = 'tempo'
client = sh.ScrapinghubClient(apikey)
project_id = config['scrapinghub']['project_id']
spider_id = 2
job_id = 42

nro = u'{}/1'.format(str(client.projects.list()[0]))
# Job key should consist of project_id/spider_id/job_id

# job = client.get_job(
# 	u'{}/{}/{}'.format(project_id,spider_id,job_id)
# 	)
# for item in job.items.iter():
# 	print(item)

# print(client.projects.summary())
listas = []
project = client.get_project(project_id)
# for i in project.spiders.list():
# 	dicionario = {}
# 	spider = project.spiders.get(i['id'])
# 	dicionario = {spider.key : spider.name}
# 	listas.append(dicionario)
	# print(spider.key,spider.name)

[listas.append({'key': project.spiders.get(i['id']).key,'name' : project.spiders.get(i['id']).name}) \
for i in project.spiders.list()]

[print(x['key'],x['name']) for x in listas]
# print(data)

'''
# spider = spider.jobs.run(spider)
spider = project.spiders.get(spider_)

job = spider.jobs.run()

spider.jobs.summary()

for item in job.items.iter():
	print(item)
'''