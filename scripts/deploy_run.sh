gcloud run deploy process-task-service \
    --image gcr.io/your-project-id/process-task-service \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars BUCKET_NAME=your-bucket-name