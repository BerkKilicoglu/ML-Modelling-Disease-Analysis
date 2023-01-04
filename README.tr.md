## ML Modelling - Disease Analysis

[![Build Status](https://img.shields.io/badge/lang-T%C3%BCrk%C3%A7e-red)](https://github.com/BerkKilicoglu/ML-Modelling-Disease-Analysis/blob/main/README.tr.md) [![Build Status](https://img.shields.io/badge/lang-English-blue)](https://github.com/BerkKilicoglu/ML-Modelling-Drug-Disease-Analysis/blob/main/README.md)

> **Note:** Bu depoda makine öğrenimi merkezli detaylı analiz yapılmıştır. Sizde farklı veri setlerinde ve farklı problemleri çözmek için uygun şekilde modifiye edip kullanabilirsiniz.

`./dataset`: dizin ***.xlsx*** formatında verisetini içerir. Veriseti sadece 2 tür sınıf içermektedir. Boş değerler kontrol edilmiştir.

> **Note**: 
> `grid_search.py` hiper parametre taraması yapar, verilen parametre sayısına göre kodun yürütme süresi uzun olabilir. ./results dizini içerisinde; önceden kendi çalıştırmalarımla elde ettiğim grid search sonuçlarına göz atabilirsiniz.



 - Orijinal veri seti [***Diabetes Health Indicators Dataset***](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

### Veri Kümesi Bilgileri

Veri seti, Diabet hasatalığı tanıları için 21 faktörü içermektedir. Toplam 70692 kişinin ölçümlerini içermektedir.

Özellikler:
Diabetes_binary: Kişinin diabet durumunu belirtir.
HighBP: Yüksek kan basıncı (0:yüksek değil, 1:yüksek)
HighChol: Yüksek kolestrol değeri (0:yüksek değil, 1:yüksek)
CholCheck: Kolestrol kontrol durumu (0:5 yıl içinde yaptırmamış, 1:5yıl içinde yaptırmış)
BMI: Vücut Kitle İndeksi
Smoker: Hayatınız boyunca en az 100 sigara içtiniz mi? (0:hayır 1:evet)
Stroke: Felç geçirme durumu (0:hayır 1:evet)
HeartDiseaseorAttack: Koroner kalp hastalığı veya miyokard enfarktüsü (0:hayır 1:evet)
PhysActivity: Son 30 gündeki fiziksel aktivite - iş dahil değil (0:hayır 1:evet)
Fruits: Günde 1 veya daha fazla meyve tüketimi (0:hayır 1:evet)
Veggies: Günde 1 veya daha fazla sebze tüketin (0:hayır 1:evet)
HvyAlcoholConsump: Ağır alkol tüketimi varmı? (0:hayır 1:evet)
AnyHealthcare: Herhangi bir sağlık sigortası varmı? (0:hayır 1:evet)
NoDocbcCost: Son 12 ayda bir doktora görünmeniz gerekip de maliyet nedeniyle gidemediğiniz bir zaman oldu mu? (0:hayır 1:evet)
GenHlth: Genel olarak sağlığınızın: 1-5 ölçeği 1 = mükemmel 2 = çok iyi 3 = iyi 4 = orta 5 = kötü olduğunu söyleyebilir misiniz?
MentHlth: Son 30 günde ruhsal sağlık sorunu yaşanan gün sayısı.
PhysHlth: Son 30 günde fiziksel sağlık sorunu yaşanan gün sayısı.
DiffWalk: Yürürken veya merdiven çıkarken ciddi zorluk çekiyor musunuz? (0:hayır 1:evet)
Sex: Cinsiyet (0:Kadın, 1:Erkek)
Age: 13 seviyeli yaş kategorisi (1 = 18-24, 9 = 60-64, 13 = +80 yaş)
Education: Eğitim seviyesi
Income: Gelir düzeyi 1= 10.000$ 8= +75.000$