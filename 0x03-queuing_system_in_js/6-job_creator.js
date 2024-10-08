import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0802190',
  message: 'This is a push notification test message',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Error creating notification job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
