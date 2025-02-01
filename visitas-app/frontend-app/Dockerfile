# Etapa de build
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --prod

# Etapa de producción con Nginx
FROM nginx:alpine
COPY --from=build /app/dist/frontend-app /usr/share/nginx/html

# Asegurar que Nginx use el index.html de Angular
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
