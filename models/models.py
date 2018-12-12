
def create_model(opt):
    model = None
    print(opt.model)
    if opt.model == 'shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.shift_net.shiftnet_model import ShiftNetModel
        model = ShiftNetModel()

    elif opt.model == 'accelerated_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.accelerated_shift_net.accelerated_shiftnet_model import ShiftNetModel
        model = ShiftNetModel()

    elif opt.model == 'soft_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.soft_shift_net.soft_shiftnet_model import ShiftNetModel
        model = ShiftNetModel()

    elif opt.model == 'test':
        assert(opt.dataset_mode == 'single')
        from .test_model import TestModel
        model = TestModel()
    else:
        raise ValueError("Model [%s] not recognized." % opt.model)
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))
    return model
