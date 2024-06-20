from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve 