from st2actions.runners.pythonrunner import Action

class generateNamingConvention(Action):
 def run(self,projectCategory,description,API,componentName,projectFacing):
    self.logger.info("GitLab repository creation completed")
    if projectFacing == "internal" :
            projectFqdn="com.rxcorp."
    else:
            projectFqdn="com.quintilesims."
    if API is None:
            projectName=(projectFqdn+projectCategory+'.'+componentName).lower()
    else:
         projectName=(projectFqdn+projectCategory+'.'+componentName+'.'+API).lower()
    return {"projectName": projectName,"Category": projectCategory}



