<p align="center">
  <img width="414" alt="yfitops" src="https://github.com/svaret/yfitops/blob/master/static/yfitops.png">
</p>

Setup:
- install brew
- brew install python3
- pip3 install flask
- export PATH=$PATH:/Users/pekr/Library/Python/3.8/bin

How to get random album cover for an artist, exchange "pinchers" for "your" artist:

- http://localhost:5000?artist=pinchers

Responsive development help:

- https://codepen.io/supergillie/pen/PoBPerJ

How to deploy to pythonanywhere from localhost:

- Add the remote repo @ pythonanywhere: 
  git remote add pythonanywhere vinylbingo@ssh.pythonanywhere.com:/home/vinylbingo/bare-repos/yfitops.git
- Push code to pythonanywhere:
  git push -u pythonanywhere master 
- Read more => https://blog.pythonanywhere.com/87/

How to deploy to pythonanywhere:
- https://www.youtube.com/watch?v=75-oCKUx3oU

How to deploy flask application to Amplify: 
- https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/
- https://acloudguru.com/blog/engineering/create-a-serverless-python-api-with-aws-amplify-and-flask

How to get around request quota limit at Discogs: 

- https://www.discogs.com/forum/thread/732352
