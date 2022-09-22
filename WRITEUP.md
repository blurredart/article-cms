> I chose to go with Azure App services for deploying the Article CMS application.

1. **Cost**: VMs is more expensive than App services. But since we don't require that control that VM gives us for deploying our app, we can go with App services
2. **Scalability**: Azure provides facility to scale by deploying more instances of App service which improves scalability when required. We can also improve throughput using vertical scaling by choosing compute instances with better resources such as RAM/CPU
3. **Availability**: Due to shared responsibility model, when using App services, the customer need not maintain SQL server or the underlying operating system. This improves availability since Azure takes care of keeping the service available where as developer can focus on Application itself.
4. **Workflow**: Again, since user is not maintaining database server or the underlying OS on which our app is deployed, this simplifies the workflow in terms of time and knowledge needed for developers. This also improves the time required to deploy our to production when new features are added.

*If we want our app service to be able to be able to be deployed on particular operating system or have to support running our app on multiple operating systems and want to have more control over how our app is deployed, it is better to choose Azure VM for deploying or compute workload. But since our app doesn't require that flexibility, we can choose to continue with Azure App service.*


