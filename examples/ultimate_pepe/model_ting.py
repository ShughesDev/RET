#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:38:17 2023

@author: Shugsy

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

⠀⠀⢀⣠⠤⠶⠖⠒⠒⠶⠦⠤⣄⠀⠀⠀⣀⡤⠤⠤⠤⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣦⠞⠁⠀⠀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡾⠁⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠚⠉⠁⠀⠀⠀⠀⠈⠉⠙⠲⣄⣤⠤⠶⠒⠒⠲⠦⢤⣜⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠹⣆⠀⠀⠀⠀⠀⠀⣀⣀⣀⣹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⣉⣡⠤⠴⠿⠗⠳⠶⣬⣙⠓⢦⡈⠙⢿⡀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡿⣷⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣡⠞⣁⣀⣀⣀⣠⣤⣤⣤⣄⣭⣷⣦⣽⣦⡀⢻⡄⠰⢟⣥⣾⣿⣏⣉⡙⠓⢦⣻⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠙⠻⢤⣄⣼⣿⣽⣿⠟⠻⣿⠄⠀⠀⢻⡝⢿⡇⣠⣿⣿⣻⣿⠿⣿⡉⠓⠮⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢦⡈⠛⠿⣾⣿⣶⣾⡿⠀⠀⠀⢀⣳⣘⢻⣇⣿⣿⣽⣿⣶⣾⠃⣀⡴⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⢄⣈⣉⣙⣓⣒⣒⣚⣉⣥⠟⠀⢯⣉⡉⠉⠉⠛⢉⣉⣡⡾⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⠋⠀⠀⠀⠀⠈⠻⣍⠉⠀⠺⠿⠋⠙⣦⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣥⣤⠴⠆⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀
⠸⢫⡟⠙⣛⠲⠤⣄⣀⣀⠀⠈⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⣨⠇⠀⠀⠀⠀⠀
⠀⠀⠻⢦⣈⠓⠶⠤⣄⣉⠉⠉⠛⠒⠲⠦⠤⠤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⠴⢋⡴⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠓⠦⣄⡀⠈⠙⠓⠒⠶⠶⠶⠶⠤⣤⣀⣀⣀⣀⣀⣉⣉⣉⣉⣉⣀⣠⠴⠋⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠒⠒⠒⠒⠒⠤⠤⠤⠒⠒⠒⠒⠒⠒⠚⢉⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠛⠳⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠚⠁⠀⠀⠀⠀⠘⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠙⢷⡋⢙⡇⢀⡴⢒⡿⢶⣄⡴⠀⠙⠳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠈⠛⢻⠛⢉⡴⣋⡴⠟⠁⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠘⣶⢋⡞⠁⠀⠀⢀⡴⠂⠀⠀⠀⠀⠹⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⠻⢦⡀⠀⣰⠏⠀⠀⢀⡴⠃⢀⡄⠙⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⢷⡄⠀⠀⠀⠀⠉⠙⠯⠀⠀⡴⠋⠀⢠⠟⠀⠀⢹⡄

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
###### Imports
### General
from __future__ import annotations

import os
from datetime import datetime, timedelta

### RET
from mesa_ret.model import RetModel

from mesa_ret.space.space import ContinuousSpaceWithTerrainAndCulture3d
from mesa_ret.space.culture import Culture
from mesa_ret.space.heightband import AbsoluteHeightBand

from mesa_ret.batchrunner import FixedReportingBatchRunner

### Pepe Model
from pepe_agent import PepeAgent

###### Model

class PepeModel(RetModel):
    """
    And on that fateful day it was decided...
    
    Pepe the Brutal was victorious (?)
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    =
    =    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣠⣤⡶⠶⠿⠿⠶⢶⣤⣄⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣦⣶⠿⠛⠉⠉⠁⠀⠈⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣀⡀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⣶⡿⠛⠉⠀⠀⠀⠀⠀⠈⠉⠻⢷⣿⣧⣶⣶⠶⠿⠿⠿⠿⠷⣶⣾⣷⣄⡀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⣠⣤⣶⠶⢾⣿⣿⡿⠿⣶⣄⠀⠀⢴⡶⠶⡶⣷⣾⢿⠿⠿⠷⣦⣄⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡟⠀⠀⠀⠀⠀⠀⣀⣤⣶⠾⣻⣭⣷⠾⠛⠛⠋⠛⠛⠛⠻⢿⣷⣤⣶⣷⠶⠿⡛⣛⢛⠛⠛⠿⣶⣿⡆⠀
    =⠀⠀⠀⠀⠀⢀⣴⡾⠛⠁⠀⠀⠀⠀⠀⢠⣴⣿⣭⡶⠟⠋⠉⠀⣀⣠⣤⣶⣶⠾⠿⠛⠻⢿⣧⣤⣴⡶⠿⢿⣿⣿⣿⣟⠛⠷⠿⣿⡆
    =⠀⠀⠀⠀⠀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⠾⣷⣶⣶⡶⠾⠛⢻⣿⣏⣻⡿⠻⣦⡀⢀⣼⠏⠁⠀⠀⢠⣿⣧⣼⠛⣿⣷⠀⢀⣼⡇
    =⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣯⣛⡷⣦⣤⣾⣿⣯⣽⣷⣴⣿⡷⣟⣿⠷⠶⣶⣤⣾⣿⣦⣿⣶⣿⣿⣿⣿⠏⠀
    =⠀⠀⣠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⠿⠿⠿⠷⢾⣿⣿⠟⠋⠁⣤⡀⠀⠀⠀⠀⠀⠀⢀⣠⣼⠟⠀⠀⠀
    =⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡶⠿⠋⠁⠀⠀⠀⠛⠻⢶⣶⡶⠶⠶⠿⣿⡏⠁⠀⠀⠀⠀
    =⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀
    =⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀
    =⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠶⡿⠛⠛⠻⠿⠶⢶⣦⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣤⣤⣶⠶⠟⠻⣧⠀⠀
    =⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡟⠀⠰⡶⢶⣶⣶⣤⣤⣤⣀⣀⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠀⠀⢀⣀⣴⡟⠀⠀
    =⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠘⢿⣤⣀⣥⣤⣴⣦⣤⣬⣉⣉⣛⠛⠛⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠟⠛⢻⣿⠁⠀⠀⠀
    =⠀⠀⠈⠻⣧⣄⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣉⡉⠁⠀⠀⠀⠀⠈⠉⠛⠛⠻⠿⠿⠶⢶⣶⣶⣶⣦⣤⣤⣤⣄⣠⣤⣴⡾⠋⠀⠀⠀⠀
    =⠀⠀⠀⠀⠘⢿⣷⣦⣤⣀⡀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣽⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⡷⣶⣦⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣴⣶⡾⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⠾⢯⣭⣭⣭⣭⣉⣉⣉⣉⣉⣉⣉⣩⣭⣽⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    =⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """
    def __init__(self) -> None:
        """
        Initialise that b fo sho my g.
        """
        super().__init__(
            start_time = datetime(2023, 9, 4, 21, 43),
            time_step = timedelta(seconds = 30),
            end_time = datetime(2023, 9, 5, 0, 0),
            space = self.set_up_space(),
            )
        
        self.height_bands = [
            AbsoluteHeightBand("500m", 500),
            AbsoluteHeightBand("2000m", 2000),
            AbsoluteHeightBand("12000m", 12000),
            ]
        
        self.pepe = self.create_the_pepe() #create the one true pepe
        self.hostile_agents = self.create_hostile_agents() #create hostile agents
        
    def set_up_space(self) -> ContinuousSpaceWithTerrainAndCulture3d:
        """
        Set up the simulated space. Includes:
            - x/y limits
            - image paths for terrain (culture) and height maps
            - sets what heights varying shades of grey represent
            - sets what cultures are which colours
        
        Two housefrogges, both alike in ribbity
        (In fair Continious space with terrain and culture 3d, where we lay our scene),
        From ancient grudge break to new mutiny,
        Where civil blood makes civil frogges unclean.
        """
        return ContinuousSpaceWithTerrainAndCulture3d(
            x_max = 46500,#m
            y_max = 33700,#m
            terrain_image_path = os.path.join("images", "grenouille_de_couleur_mort.png"),
            height_black = 0.0,
            height_white = 0.0,
            culture_image_path = os.path.join("images", "grenouille_de_couleur_minimale.png"),
            culture_dictionary={
                (0, 255, 0): Culture("land"),#verte
                (0, 0, 255): Culture("land"),#bleue
                (255, 0, 0): Culture("land"),#rouge
                (0, 0, 0): Culture("land"),#blanche
                (255, 255, 255): Culture("land"),#noire
                (255, 0, 255): Culture("land"),#rose
                (0, 255, 255): Culture("land"),#turquoise
                (255, 255, 0): Culture("land"),#jaune
            },
        )
    
    def create_the_pepe(self) -> PepeAgent:
        """
        Pepe is essentially just an attack helicopter, but fun(-er).
        """
        return PepeAgent(model = self)
    
    def create_hostile_agents(self) -> list:
        """
        Returns list of hostile agents
        """
        
        return []
    
params = None

br = FixedReportingBatchRunner(
    model_cls = PepeModel,
    parameters_list = params,
    iterations = 1,
    max_steps = 1000,
    collect_datacollector = True,
)

br.run_all()
br.save_tables_to_csv(
    [
        "agents",
        "behaviour_log",
        "task_log",
        "trigger_log",
        "deaths",
        "shots_fired",
        "observation_record",
        "perception_record",
        "behaviour_selection",
    ]
)