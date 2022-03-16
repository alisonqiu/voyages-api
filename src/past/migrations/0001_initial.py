# Generated by Django 3.2.6 on 2022-03-09 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voyage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaptiveFate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaptiveStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Captive status',
                'verbose_name_plural': 'Captive statuses',
            },
        ),
        migrations.CreateModel(
            name='Enslaved',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('documented_name', models.CharField(blank=True, max_length=100)),
                ('name_first', models.CharField(blank=True, max_length=100, null=True)),
                ('name_second', models.CharField(blank=True, max_length=100, null=True)),
                ('name_third', models.CharField(blank=True, max_length=100, null=True)),
                ('modern_name', models.CharField(blank=True, max_length=100, null=True)),
                ('editor_modern_names_certainty', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(db_index=True, null=True)),
                ('gender', models.IntegerField(db_index=True, null=True)),
                ('height', models.DecimalField(db_index=True, decimal_places=2, max_digits=6, null=True, verbose_name='Height in inches')),
                ('skin_color', models.CharField(db_index=True, max_length=100, null=True)),
                ('last_known_date', models.CharField(blank=True, help_text='Date in format: MM,DD,YYYY', max_length=10, null=True)),
                ('last_known_date_dd', models.IntegerField(null=True)),
                ('last_known_date_mm', models.IntegerField(null=True)),
                ('last_known_year_yyyy', models.IntegerField(null=True)),
                ('dataset', models.IntegerField(db_index=True, default=0)),
                ('notes', models.CharField(max_length=8192, null=True)),
                ('captive_fate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='past.captivefate')),
                ('captive_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='past.captivestatus')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('is_multilingual', models.BooleanField(default=False)),
                ('status', models.IntegerField()),
                ('token', models.CharField(blank=True, max_length=40, null=True)),
                ('contributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('enslaved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.enslaved')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavementRelation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.CharField(help_text='Date in MM,DD,YYYY format with optional fields.', max_length=12, null=True)),
                ('date_dd', models.IntegerField(null=True)),
                ('date_mm', models.IntegerField(null=True)),
                ('date_yyyy', models.IntegerField(null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('text_ref', models.CharField(blank=True, help_text='Source text reference', max_length=255)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='voyage.place')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavementRelationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Enslaver alias',
            },
        ),
        migrations.CreateModel(
            name='EnslaverIdentity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_alias', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(null=True)),
                ('birth_month', models.IntegerField(null=True)),
                ('birth_day', models.IntegerField(null=True)),
                ('birth_place', models.CharField(max_length=255, null=True)),
                ('death_year', models.IntegerField(null=True)),
                ('death_month', models.IntegerField(null=True)),
                ('death_day', models.IntegerField(null=True)),
                ('death_place', models.CharField(max_length=255, null=True)),
                ('father_name', models.CharField(max_length=255, null=True)),
                ('father_occupation', models.CharField(max_length=255, null=True)),
                ('mother_name', models.CharField(max_length=255, null=True)),
                ('first_spouse_name', models.CharField(max_length=255, null=True)),
                ('first_marriage_date', models.CharField(max_length=12, null=True)),
                ('second_spouse_name', models.CharField(max_length=255, null=True)),
                ('second_marriage_date', models.CharField(max_length=12, null=True)),
                ('probate_date', models.CharField(max_length=12, null=True)),
                ('will_value_pounds', models.CharField(max_length=12, null=True)),
                ('will_value_dollars', models.CharField(max_length=12, null=True)),
                ('will_court', models.CharField(max_length=12, null=True)),
                ('text_id', models.CharField(max_length=50)),
                ('first_active_year', models.IntegerField(null=True)),
                ('last_active_year', models.IntegerField(null=True)),
                ('number_enslaved', models.IntegerField(null=True)),
                ('principal_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voyage.place')),
            ],
            options={
                'verbose_name': 'Enslaver unique identity and personal info',
            },
        ),
        migrations.CreateModel(
            name='EnslaverMerger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_alias', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(null=True)),
                ('birth_month', models.IntegerField(null=True)),
                ('birth_day', models.IntegerField(null=True)),
                ('birth_place', models.CharField(max_length=255, null=True)),
                ('death_year', models.IntegerField(null=True)),
                ('death_month', models.IntegerField(null=True)),
                ('death_day', models.IntegerField(null=True)),
                ('death_place', models.CharField(max_length=255, null=True)),
                ('father_name', models.CharField(max_length=255, null=True)),
                ('father_occupation', models.CharField(max_length=255, null=True)),
                ('mother_name', models.CharField(max_length=255, null=True)),
                ('first_spouse_name', models.CharField(max_length=255, null=True)),
                ('first_marriage_date', models.CharField(max_length=12, null=True)),
                ('second_spouse_name', models.CharField(max_length=255, null=True)),
                ('second_marriage_date', models.CharField(max_length=12, null=True)),
                ('probate_date', models.CharField(max_length=12, null=True)),
                ('will_value_pounds', models.CharField(max_length=12, null=True)),
                ('will_value_dollars', models.CharField(max_length=12, null=True)),
                ('will_court', models.CharField(max_length=12, null=True)),
                ('text_id', models.CharField(max_length=50)),
                ('first_active_year', models.IntegerField(null=True)),
                ('last_active_year', models.IntegerField(null=True)),
                ('number_enslaved', models.IntegerField(null=True)),
                ('comments', models.CharField(max_length=1024)),
                ('principal_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voyage.place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnslaverRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, null=True, verbose_name='Longitude of point')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, null=True, verbose_name='Latitude of point')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegisterCountry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Register country',
                'verbose_name_plural': 'Register countries',
            },
        ),
        migrations.CreateModel(
            name='ModernCountry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitude of Country')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitude of Country')),
                ('languages', models.ManyToManyField(to='past.LanguageGroup')),
            ],
            options={
                'verbose_name': 'Modern country',
                'verbose_name_plural': 'Modern countries',
            },
        ),
        migrations.CreateModel(
            name='EnslaverVoyageConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField()),
                ('order', models.IntegerField(null=True)),
                ('enslaver_alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.enslaveralias')),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverMergerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enslaver_identity_id', models.IntegerField()),
                ('merger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.enslavermerger')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverInRelation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('enslaver_alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='past.enslaveralias')),
                ('role', models.ForeignKey(help_text='The role of the enslaver in this relation', null=True, on_delete=django.db.models.deletion.CASCADE, to='past.enslaverrole')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslavers', to='past.enslavementrelation')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverIdentitySourceConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_order', models.IntegerField()),
                ('text_ref', models.CharField(blank=True, max_length=255)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslaver_sources', to='past.enslaveridentity')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslaver_identity', to='voyage.voyagesources')),
            ],
        ),
        migrations.AddField(
            model_name='enslaveralias',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.enslaveridentity'),
        ),
        migrations.AddField(
            model_name='enslavementrelation',
            name='relation_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.enslavementrelationtype'),
        ),
        migrations.AddField(
            model_name='enslavementrelation',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.voyagesources'),
        ),
        migrations.AddField(
            model_name='enslavementrelation',
            name='voyage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.voyage'),
        ),
        migrations.CreateModel(
            name='EnslavedSourceConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_order', models.IntegerField()),
                ('text_ref', models.CharField(blank=True, max_length=255)),
                ('enslaved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources_conn', to='past.enslaved')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.voyagesources')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=3)),
                ('recordings_count', models.IntegerField()),
            ],
            options={
                'unique_together': {('name', 'language')},
            },
        ),
        migrations.CreateModel(
            name='EnslavedInRelation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('enslaved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='past.enslaved')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslaved_person', to='past.enslavementrelation')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedContributionNameEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.enslavedcontribution')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedContributionLanguageEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.enslavedcontribution')),
                ('language_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.languagegroup')),
            ],
        ),
        migrations.AddField(
            model_name='enslaved',
            name='language_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.languagegroup'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='post_disembark_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voyage.place'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='register_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.registercountry'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='sources',
            field=models.ManyToManyField(related_name='_past_enslaved_sources_+', through='past.EnslavedSourceConnection', to='voyage.VoyageSources'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='voyage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.voyage'),
        ),
        migrations.CreateModel(
            name='AltLanguageGroupName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('language_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alt_names', to='past.languagegroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]