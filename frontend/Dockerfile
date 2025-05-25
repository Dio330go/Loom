FROM nginx:alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy your static files to nginx's web root
COPY . /usr/share/nginx/html

# Expose port 80 (default for nginx)
EXPOSE 80