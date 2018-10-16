import mxnet as mx
import numpy as np
import cv2
from timeit import default_timer as timer
from collections import namedtuple
import csv
import os
Batch = namedtuple('Batch', ['data'])


class ImagenetModel(object):

	#Loads a pre-trained model and returns a MXNet graph
	def __init__(self, synset_path, network_prefix, context=mx.cpu(),
				 label_names=['prob_label'], input_shapes=[('data', (1, 3, 224, 224))]):

		# Load the symbols for the networks from given path
		with open(synset_path, 'r') as f:
			self.synsets = [l.rstrip() for l in f]

		# Load the network parameters from default epoch 0
		sym, arg_params, aux_params = mx.model.load_checkpoint(network_prefix, 0)

		# Load the network into an MXNet module and bind the corresponding parameters
		self.mod = mx.mod.Module(symbol=sym, label_names=label_names, context=context)
		self.mod.bind(for_training=False, data_shapes=input_shapes)
		self.mod.set_params(arg_params, aux_params)

	def predict_from_image(self, cvimage, filepath, reshape=(224, 224), N=5):
		topN = []
		imageheight, imagewidth = cvimage.shape[0:2]
		
		t1 = timer()

		# Switch RGB to BGR format (which ImageNet networks take)
		img = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
		if img is None:
			return topN
		
		img = cv2.resize(img, reshape)
		img = np.swapaxes(img, 0, 2)
		img = np.swapaxes(img, 1, 2)
		img = img[np.newaxis, :]
		
		t2 = timer()
		
		self.mod.forward(Batch([mx.nd.array(img)]))
		prob = self.mod.get_outputs()[0].asnumpy()
		prob = np.squeeze(prob)

		t3 = timer()
		
		#print("Filename {} with size {} converted in {} and forward prop done in {}".format(filepath, imageheight, t2-t1, t3-t2))
		with open('all_timings_35_vgg16.txt', 'a') as csv_file:
			employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			employee_writer.writerow([filepath.split(os.sep)[-1], os.path.getsize(filepath), imagewidth, imageheight, t1, t2, t3])
			
		
		a = np.argsort(prob)[::-1]
		for i in a[0:N]:
			topN.append((prob[i], self.synsets[i]))
		return topN