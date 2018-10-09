import tensorflow as tf
import numpy as np

inputs = tf.placeholder(tf.float32, [2,6])
lens = tf.placeholder(tf.int32, [None])
normal_rv = tf.Variable( tf.truncated_normal([2,3],stddev = 0.1))

pad = tf.pad(inputs, [[0,0],[1,0]], constant_values=1)
rev = tf.reverse_sequence(inputs, seq_lengths=lens, seq_dim=1)
slice = inputs[:,0]
bools = tf.equal(inputs, 0)

#print(len(inputs))
sz = tf.size(inputs)
shape = tf.shape(inputs)[0]

sess = tf.InteractiveSession()
sample = np.random.random([2,6])


sample_lens = np.array(sample.shape, np.int32)
sample_lens.fill(sample.shape[1])
sum = tf.reduce_sum(pad,axis=0)
print(sample)
init_op = tf.initialize_all_variables()
sess.run(init_op)
out = sess.run([pad, rev, sum, slice, bools, sz, shape], {inputs: sample, lens: sample_lens})
print(sess.run(normal_rv))


# sig cross entr
p = tf.placeholder(tf.float32, shape=[None, 2])
logits = tf.placeholder(tf.float32, shape=[None, 2])
q = tf.sigmoid(logits)
#q = tf.nn.softmax(logits)

feed_dict = {
  p: [[0, 1],  # 1-hot labels
      [1, 0]],
  logits: [[0.2, 0.8],   # output
            [0.7, 0.3]]
           }

# to compute softmax
#e = tf.exp(logits)
#s = tf.reduce_sum(e)
#q = e/s
ce = p * tf.log(q)
loss = -tf.reduce_sum(ce,axis=1)
#x = tf.matmul(p,tf.log(q),transpose_b=True)
prob1 = -tf.reduce_sum(p * tf.log(q), axis=1)
prob2 = tf.nn.softmax_cross_entropy_with_logits(labels=p, logits=logits)
prob3 = tf.nn.sigmoid_cross_entropy_with_logits(labels=p, logits=logits)

out = sess.run([prob1, prob2, prob3, loss], feed_dict)

print(out)    