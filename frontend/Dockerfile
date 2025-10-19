FROM node:20-alpine

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json* ./
RUN npm install --legacy-peer-deps || yarn || true

# Copy the rest of the frontend source code
COPY . .

RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "dev"]
