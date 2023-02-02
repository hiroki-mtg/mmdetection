_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

# 1. dataset settings
dataset_type = 'CocoDataset'
classes = ('pip-1', 'pip-10', 'pip-11', 'pip-12', 'pip-2', 'pip-3', 'pip-4', 'pip-5', 'pip-6', 'pip-7', 'pip-8', 'pip-9')
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file='path/to/your/train/annotation_data',
        img_prefix='path/to/your/train/image_data'),
    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file='path/to/your/val/annotation_data',
        img_prefix='path/to/your/val/image_data'),
    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file='path/to/your/test/annotation_data',
        img_prefix='path/to/your/test/image_data'))


# 2. model settings
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=12,
        )))
        