import createPushNotificationsJobs from '8-job';
import kue from 'kue';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', function () {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw error if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue).to.throw('Jobs is not an array');
  });

  it('should create jobs for each item in jobs', function () {
    const jobs = [
      { phoneNumber: '06712909', message: 'first Test message' },
      { phoneNumber: '32828978', message: 'second Test message' }
    ];

    createPushNotificationsJobs(jobs, queue);

   expect(queue.testMode.jobs.length).to.equal(2);
   expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
   expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
   expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
});


