from st2actions.runners.pythonrunner import Action
import gitlab

class createGitlabRepository(Action):
def run(self,projectName,description,groupId):
gitLabUrl=self.config["gitLabUrl"]
gitLabUserName=self.config["gitLabUsername"]
gitLabPrivateToken=self.config["gitLabPrivateToken"]
connectGitLab = gitlab.Gitlab(gitLabUrl,gitLabPrivateToken,ssl_verify=False)
self.logger.info('Connecting to GitLab')
connectGitLab.auth()
self.logger.info(connectGitLab.auth()
gitLabRepoCreationStatus=connectGitLab.projects.create({'name': projectName, 'default_branch': 'master', 'wiki_enabled': 1, 'namespace_id': groupId})
self.logger.info('Created repo')
self.logger.info(gitLabRepoCreationStatus)
gitLabProjectId=gitLabRepoCreationStatus.id
gitLabProjectSshUrl=gitLabRepoCreationStatus.ssh_url_to_repo
self.logger.info('Creating gitFlow branches')
self.logger.info('Creating develop Branch')
self.logger.info("GitLab repository creation completed")
gitStringWithSSHUrl=gitLabProjectSshUrl.replace('[','ssh://')
finalSshString=gitStringWithSSHUrl.replace(']:',"/")
return {"RepositoryUrl": finalSshString,"gitlabProjectId": gitLabProjectId}



