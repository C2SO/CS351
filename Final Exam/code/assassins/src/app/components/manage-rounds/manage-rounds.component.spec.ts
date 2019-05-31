import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageRoundsComponent } from './manage-rounds.component';

describe('ManageRoundsComponent', () => {
  let component: ManageRoundsComponent;
  let fixture: ComponentFixture<ManageRoundsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManageRoundsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManageRoundsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
