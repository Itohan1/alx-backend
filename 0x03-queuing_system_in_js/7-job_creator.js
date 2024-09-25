import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach((job) => {
  const newjob = queue.create('push_notification_code_2', job)
    .save((err) => {
      if (err) {
        console.error('Error creating notification job:', err);
      } else {
        console.log(`Notification job created: ${newjob.id}`);
      }
    });

    newjob.on('complete', () => {
      console.log(`Notification job ${newjob.id} completed`);
    });

    newjob.on('failed', (err) => {
      console.error(`Notification job ${newjob.id} failed:`, err);
    });

    newjob.on('progress', (progress) => {
      console.log(`Notification job ${newjob.id} ${progress}% complete`);
    });

});
