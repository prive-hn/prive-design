FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY DESIGN.md /usr/share/nginx/html/DESIGN.md
COPY banners.html /usr/share/nginx/html/banners.html
COPY assets/ /usr/share/nginx/html/assets/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]