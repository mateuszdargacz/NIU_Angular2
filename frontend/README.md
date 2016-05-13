
### Quick start Frontend
**Make sure you have Node version >= 4.0 and NPM >= 3**
> Clone/Download the repo then edit `app.ts` inside [`/src/app/app.ts`](/src/app/app.ts)

```bash

# add required global libraries
npm install typings webpack-dev-server rimraf webpack -g

# install the repo with npm
npm install

# start the server
npm start

# use Hot Module Replacement
npm run server:dev:hmr

```
go to [http://0.0.0.0:3000](http://0.0.0.0:3000) or [http://localhost:3000](http://localhost:3000) in your browser

# Getting Started
## Dependencies
What you need to run this app:
* `node` and `npm` (`brew install node`)
* Ensure you're running the latest versions Node `v4.x.x`+ (or `v5.x.x`) and NPM `3.x.x`+

Once you have those, you should install these globals with `npm install --global`:
* `webpack` (`npm install --global webpack`)
* `webpack-dev-server` (`npm install --global webpack-dev-server`)
* `karma` (`npm install --global karma-cli`)
* `protractor` (`npm install --global protractor`)
* `typings` (`npm install --global typings`)
* `typescript` (`npm install --global typescript`)


# Quickstart Backend
## Dependencies

* `virtualenv env --no-site-packages`
* `env/bin/activate`
* `pip install requrements.txt`

## Setup

* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py runserver`

Server is ready to go at 0.0.0.0:8000



