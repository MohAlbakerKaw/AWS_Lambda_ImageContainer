# AWS_Lambda_ImageContainer
In usual scenarios, the proposed system by a machine learning engineer/s must be economical, fast-deployed, mobile (able to run anywhere), and scalable. <br>
Recently and after the release of AWS lambda based on a container image, -to my mind- it is one of the most efficient ways to take your model to production.<br>
The idea behind AWS lambda is that you can upload and run your code without thinking about the server running it. <br>
latterly, you can package and deploy your Lambda function as a container image of up to 10 GB in size. <br>
This way, you benefit from operational simplicity, automatic scaling, high availability, cost-effectiveness, and native integrations with other services.<br>
Two main issues while using Lambda:<br>
1- Lambdas have a timeout limit of 15 minutes, which means that your entire model interactions are supposed to be less than the time limit (if your model is huge or you are dealing with big data, Lambda won't be a good choice). Nonetheless, you can create multiple lambdas and orchestrate them using a Step function.<br>
2- Cold-start delay, Lambdas incurs a cold-start latency when the function is invoked after some period of inactivity. "According to an analysis of production Lambda workloads, cold starts typically occur in under 1% of invocations. The duration of a cold start varies from under 100 ms to over 1 second.." {quoted from a post by James Beswick}.<br>
In the attached repo, I tried to make it simple and straight to take your code into production with Lambda from the image container. <br>
The main notebook lists the steps to follow, and smoothly you can adjust the code, build an image, push to the elastic container registry ECR, and deploy it as a lambda function.<br>
