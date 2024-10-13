# Backend
## Vercel production
[Deployment Repo](https://github.com/THDCPL/Backend)

[URL](https://backend-liard-one.vercel.app)

`https://backend-liard-one.vercel.app`

## Local Development
1. Run `docker compose build`
2. Run `docker compose up -d Postgres` to start DB container
3. Launch Debuger FastAPI in VSCode

## Vercel Deployment
You can deploy app on your Vercel account executing following steps:
1. install `vercel-cli`
2. run `vercel --prod`
3. (Optional) If it is the first deployment, you need to open project `Storage -> Create Database -> Postgres`

## Local Deployment
1. Run `docker compose build`
2. Run `docker compose up -d`

Database container uses a volume, so to remove it u need to add `-v` flag to command `docker compose down`