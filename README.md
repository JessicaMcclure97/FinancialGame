This is information on how to run the website. Note that the backend needs to run before the frontend.

** BACKEND **

```
cd /FinancialGame/backend/ 
source environment/bin/activate

cd server 
python manage.py runserver 
```

** FRONTEND **

```
cd /FinancialGame/frontend/game/
npm install --legacy-peer-deps
npm start
```
These are some of the npm files that may need to be installed:
npm install -S react95 styled-components
npm install react-plotly.js
