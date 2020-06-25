import argparse
from unittest import TestCase

import pytorch_lightning as pl

from pl_bolts.models.rl.common import cli
from pl_bolts.models.rl.double_dqn.double_dqn_model import DoubleDQN
from pl_bolts.models.rl.dqn.dqn_model import DQN
from pl_bolts.models.rl.dueling_dqn.dueling_dqn_model import DuelingDQN
from pl_bolts.models.rl.n_step_dqn.n_step_dqn_model import NStepDQN
from pl_bolts.models.rl.noisy_dqn.noisy_dqn_model import NoisyDQN
from pl_bolts.models.rl.per_dqn.per_dqn_model import PERDQN


class TestValueModels(TestCase):

    def setUp(self) -> None:
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser = cli.add_base_args(parent=parent_parser)
        parent_parser = DQN.add_model_specific_args(parent_parser)
        args_list = [
            "--algo", "dqn",
            "--warm_start_steps", "100",
            "--episode_length", "100",
            "--gpus", "0"
        ]
        self.hparams = parent_parser.parse_args(args_list)

        self.trainer = pl.Trainer(
            gpus=self.hparams.gpus,
            max_steps=100,
            max_epochs=100,  # Set this as the same as max steps to ensure that it doesn't stop early
            val_check_interval=1000  # This just needs 'some' value, does not effect training right now
        )

    def test_dqn(self):
        """Smoke test that the DQN model runs"""
        model = DQN(self.hparams.env)
        result = self.trainer.fit(model)

        self.assertEqual(result, 1)

    def test_double_dqn(self):
        """Smoke test that the Double DQN model runs"""
        model = DoubleDQN(self.hparams.env)
        result = self.trainer.fit(model)

        self.assertEqual(result, 1)

    def test_dueling_dqn(self):
        """Smoke test that the Dueling DQN model runs"""
        model = DuelingDQN(self.hparams.env)
        result = self.trainer.fit(model)

        self.assertEqual(result, 1)

    def test_noisy_dqn(self):
        """Smoke test that the Noisy DQN model runs"""
        model = NoisyDQN(self.hparams.env)
        result = self.trainer.fit(model)

        self.assertEqual(result, 1)

    def test_per_dqn(self):
        """Smoke test that the PER DQN model runs"""
        model = PERDQN(self.hparams.env)
        result = self.trainer.fit(model)

        self.assertEqual(result, 1)

    def test_n_step_dqn(self):
        """Smoke test that the N Step DQN model runs"""
        model = NStepDQN(self.hparams.env)
        result = self.trainer.fit(model)

        self.assertEqual(result, 1)
