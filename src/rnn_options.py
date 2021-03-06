class Options(object):
    model_type = "retain_general"   # retain_general, retain_only_chart_events
    epochs = 20
    batch_size = 64
    hidden_dim = 256
    dim_emb = 256   # 128, 256
    dropout_input = 0.6
    dropout_emb = 0.6
    dim_alpha = 256
    dim_beta = 256
    dim_output = 2
    dropout_context = 0.6
    # l2 regularization
    lr = 1e-4
    weight_decay = 1e-5

