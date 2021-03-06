#
# test.py, doom-net
#
# Created by Andrey Kolishchak on 01/21/17.
#
import torch
from doom_instance import *

def test(args, model):
    print("testing...")
    model.eval()

    game = DoomInstance(args.vizdoom_config, args.wad_path, args.skiprate, visible=True)
    step_state = game.get_state_normalized()

    state = NormalizedState(screen=None, depth=None, labels=None, variables=None)
    state.screen = torch.Tensor(1, *args.screen_size)

    while True:
        # convert state to torch tensors
        state.screen[0, :] = torch.from_numpy(step_state.screen)
        # compute an action
        action = model.get_action(state)
        # render
        step_state, _, finished = game.step_normalized(action[0][0])
        if finished:
            print("episode return: {}".format(game.get_episode_return()))




