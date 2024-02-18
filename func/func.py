from flask import Flask, request, jsonify


def getExample():
    return jsonify({'success':True})