

from ultralytics import YOLO

m

# model = YOLO("OptiSAR-Net.yaml")
model = YOLO("yolov8.yaml")
# train of seaship
# model.train(data="seaship.yaml", epochs=50, imgsz=416,batch=8,optimizer="Adamax",lr0=3e-4,lrf=0.01,plots=True,val=True,save=True,close_mosaic=0)
# model.train(
#     data="seaship.yaml",
#     epochs=50,
#     imgsz=416,
#     batch=8,
#     optimizer="Adamax",
#     lr0=3e-4,
#     lrf=0.01,
#     box=7.5,
#     cls=0.5,
#     dfl=1.5,
#     kobj=1.5,

#     mosaic=0.5,
#     close_mosaic=10,
#     multi_scale=True,
#     fliplr=0.5,
#     scale=0.5,
#     conf=0.001,
#     iou=0.6,
#     fl_gamma=2.5,
#     plots=True,
#     val=True,
#     save=True
# )


model.train(
  data="seaship.yaml",
    epochs=300,
    imgsz=416,
    batch=4,

    optimizer="AdamW",
    lr0=3e-4,
    lrf=0.01,

    cos_lr=True,
    warmup_epochs=5,

    mosaic=0.7,
    close_mosaic=10,
    multi_scale=True,

    plots=True,
    val=True,
    save=True
)

# model.train(data="shipRIS.yaml", epochs=5 ,imgsz=416 ,plots=True ,val=True ,save=True, batch=8, close_mosaic=0)
# model = YOLO('last_shipRSI.pt')  # حمّلي الموديل مباشرة من .pt
# model = YOLO('OptiSAR-Net.yaml').load('last_shipRSI.pt')
# model.train(resume=True, epochs=5)
