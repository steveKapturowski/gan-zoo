# -*- coding: utf-8 -*-
import argparse
import tensorflow as tf


def main(args):
	pass


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	#defaults chosen to match paper
	parser.add_argument('--batch_size', default=64, help='Batch size for RMSProp updates', dest='batch_size')
	parser.add_argument('--epochs', default=10000, help='Number of epochs to train for', dest='num_epochs')
	parser.add_argument('--critic_steps', default=5, help='Number of steps to train the critic for each step of the generator', dest='critic_steps')
	parser.add_argument('--learning_rate', default=5e-5, help='Learning rate for optimizer', dest='learning_rate')
	parser.add_argument('--weight_clip', default=0.01, help='Clip weights at ±WEIGHT_CLIP to ensure Lipschitz constraint', dest='weight_clip')

	args = parser.parse_args()
	main(args)