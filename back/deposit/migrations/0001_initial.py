# Generated by Django 4.2.7 on 2024-05-14 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=20)),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=100)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('contract_user', models.ManyToManyField(related_name='contract_deposit', to=settings.AUTH_USER_MODEL)),
                ('like_user', models.ManyToManyField(related_name='like_deposit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=20)),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(blank=True, max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('erly_rpay_fee', models.TextField()),
                ('dly_rate', models.TextField()),
                ('loan_lmt', models.TextField()),
                ('contract_user', models.ManyToManyField(related_name='contract_loan', to=settings.AUTH_USER_MODEL)),
                ('like_user', models.ManyToManyField(related_name='like_loan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=20)),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=100)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('contract_user', models.ManyToManyField(related_name='contract_saving', to=settings.AUTH_USER_MODEL)),
                ('like_user', models.ManyToManyField(related_name='like_saving', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.CharField(max_length=2)),
                ('intr_rate_type_nm', models.CharField(max_length=10)),
                ('save_trm', models.CharField(max_length=3)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deposit.saving')),
            ],
        ),
        migrations.CreateModel(
            name='LoanOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrtg_type_nm', models.CharField(blank=True, max_length=20)),
                ('rpay_type_nm', models.CharField(max_length=20)),
                ('lend_rate_type_nm', models.CharField(max_length=20)),
                ('lend_rate_min', models.FloatField(null=True)),
                ('lend_rate_max', models.FloatField(null=True)),
                ('lend_rate_avg', models.FloatField(null=True)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deposit.loan')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('save_trm', models.CharField(max_length=3)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deposit.deposit')),
            ],
        ),
    ]
