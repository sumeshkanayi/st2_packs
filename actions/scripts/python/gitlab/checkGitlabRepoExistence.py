from st2actions.runners.pythonrunner import Action
import actions.scripts.python.gitlab

class checkGitlabRepository(Action):
    def run(self,projectName):
    #Will create a Gitlab repository .Add a README.MD file with default contents and will create Master and Developmnt branches
        repositoryExistenceFlag=0
        gitLabUrl=self.config["gitLabUrl"]
        gitLabUserName=self.config["gitLabUsername"]
        gitLabPrivateToken=self.config["gitLabPrivateToken"]
        connectGitLab = actions.scripts.python.gitlab.Gitlab(gitLabUrl, gitLabPrivateToken, ssl_verify=False)
        self.logger.info('Connecting to GitLab')
        connectGitLab.auth()
        self.logger.info(connectGitLab.auth())
        getAllGitLabProjects=connectGitLab.projects.list()
        print getAllGitLabProjects
        getAllGitLabProjectNames=[]
        for gitLabProject in getAllGitLabProjects:
            getAllGitLabProjectNames.append(gitLabProject.name)
            print gitLabProject.name
            if projectName in getAllGitLabProjectNames:
                self.logger.error("Repo exists")
                repositoryExistenceFlag=1
                return {"RepositoryExistence": "yes"}
            else:
                continue
        if repositoryExistenceFlag != 1:
            return {"RepositoryExistence": "no"}



